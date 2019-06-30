import requests
import rx
from rx import operators as op
#help(rx.concurrency)

def to_request(method, url, **kwargs):
  def subscribe(observer, dispose):
    response = requests.request(method, url, **kwargs)

    try:
      response.raise_for_status()
      observer.on_next(response)
      observer.on_completed()
    except requests.HTTPError as e:
      observer.on_error(e)
  return rx.create(subscribe)


def to_json_request(method, url, **kwargs):
  return to_request(method, url, **kwargs).pipe(
    op.map(lambda r: r.json())
  )


def to_get_json(url, **kwargs):
  return to_json_request('get', url, **kwargs)


source = rx.of(
  'http://localhost:8080?sleep=1',
  'http://localhost:8080?sleep=2',
  'http://localhost:8080?sleep=3',
)

composed = source.pipe(
  op.flat_map(to_get_json)
)

composed.subscribe(
    on_next = lambda i: print("Received {0}".format(i)),
    on_error = lambda e: print("Error Occurred: {0}".format(e)),
    on_completed = lambda: print("Done!"),
)