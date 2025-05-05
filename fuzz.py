from fuzzywuzzy import fuzz as fz
from fuzzywuzzy import process as fzpr

print(fz.ratio("hello", "bye"))


inp = "helllo"
lst = ["helo", "hello", "hellllo", "hi", "helloooo"]

print(fzpr.extractOne(inp, lst))