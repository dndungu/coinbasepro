from datetime import datetime, timedelta
import json
import requests
import time
from .ohlcv import ohlcv

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

class candles:
  def __init__(self, end=datetime.now(), product='BTC-USD', granularity=MINUTE, limit=300):
    self.end = datetime.now() if end is None else end
    self.start = end - timedelta(seconds=300*granularity)
    self.granularity = granularity
    self.limit = limit
    self.product = product
    self.data = []

  def __iter__(self):
    self.cursor = 0
    return self

  def __next__(self):
    if self.cursor < self.limit:
      if self.cursor >= len(self.data):
        time.sleep(1)
        URL = "https://api.pro.coinbase.com/products/%s/candles?granularity=%d&start=%s&end=%s"
        self.data.extend(json.loads(requests.get(URL % (self.product, self.granularity, self.start.isoformat(), self.end.isoformat())).text))
        self.end = datetime.fromtimestamp(self.data[-1][0])
        self.start = self.end - timedelta(seconds=300*self.granularity)
      x = self.data[self.cursor]
      self.cursor += 1
      return x
    else:
      raise StopIteration

  def all(self):
      return [v for v in self]

  def ohlcv(self):
      return ohlcv([v for v in reversed(self.all())])
