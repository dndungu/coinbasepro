from datetime import datetime, timedelta
import json
import requests
import time

class candles:
  MINUTE = 60
  HOUR = 60 * MINUTE
  DAY = 24 * HOUR

  def __init__(self, end=datetime.now(), product='BTC-USD', granularity=MINUTE, limit=300):
    self.end = datetime.now() if end is None else end
    self.start = end - timedelta(seconds=300*granularity)
    self.granularity = granularity
    self.limit = limit
    self.product = product
    self.ohlcv = []

  def __iter__(self):
    self.cursor = 0
    return self

  def __next__(self):
    if self.cursor < self.limit:
      if self.cursor >= len(self.ohlcv):
        time.sleep(1)
        URL = "https://api.pro.coinbase.com/products/%s/candles?granularity=%d&start=%s&end=%s"
        self.ohlcv.extend(json.loads(requests.get(URL % (self.product, self.granularity, self.start.isoformat(), self.end.isoformat())).text))
        self.end = datetime.fromtimestamp(self.ohlcv[-1][0])
        self.start = self.end - timedelta(seconds=300*self.granularity)
      x = self.ohlcv[self.cursor]
      self.cursor += 1
      return x
    else:
      raise StopIteration
