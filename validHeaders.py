#!/usr/bin/env python

class QuitError(Exception):
  pass

#takes a list of dictionaries
def label_helper(tables):
  index = 0
  def classify():
    table = tables[index]
    valid = ["True", "False", "Quit", "Undo", "Skip"]

    print(table["web data"]["headers"])
    response = input()

    if response is "Undo":
      if index >= 0:
        index -= 1
    elif response is "True" or "False":
      table["label"] = response
      index += 1
    elif response is "Skip":
      index += 1
    else:
      raise QuitError

  try:
      while True:
        classify()
    except QuitError:
      break
    except IndexError:
      print("All done.")
      break

if __name__ == "__main__":
    label_helper([{"header" : [""]}])