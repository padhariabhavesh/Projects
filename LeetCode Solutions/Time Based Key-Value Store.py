"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

"""

class TimeMap:
  def __init__(self):
    self.values = defaultdict(list)
    self.timestamps = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.values[key].append(value)
    self.timestamps[key].append(timestamp)

  def get(self, key: str, timestamp: int) -> str:
    if key not in self.timestamps:
      return ''
    i = bisect.bisect(self.timestamps[key], timestamp)
    return self.values[key][i - 1] if i > 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)