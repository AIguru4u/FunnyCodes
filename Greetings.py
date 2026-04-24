def greeting(relative):
  if relative in ("pa", "papa", "dad", "daddy", "dada", "abba", "father"):
    return "Hi dad,\nLove you!"
  elif relative in ("ma", "mama", "mom", "mommy", "amma", "mother"):
      return "Hi mom,\nLoving you!"
  elif relative in ("bro", "bruh", "bhai", "brother"):
    return "Hi bro,\nHowdy buddy"
  elif relative in ("sis", "sissy", "appi", "sister"):
    return "Hi sis,\nMy born enemie."
  elif relative in ("hubby", "hub", "husband"):
    return "Hi hubby,\nDon't even think of cheating."
  elif relative in ("wifey", "wife", "begum", "love", "honey"):
    return "Hi wifey,\nPlease spend less."
  elif relative in ("cuz", "coz", "cousin"):
    return "Hi cuz,\nWhere's party"
  elif relative in ("frnd", "fren", "buddy", "bud", "friend"):
    return "Hi friend,\nWassup."
  elif relative in ("ex"):
    return "F* off"
  elif relative in ("fi", "fiance", "bae"):
    return "Hi Love!"
  elif relative in ("gf", "babe", "bae"):
    return "Hi Love!"
  elif relative in ("bf", "babe", "bae"):
    return "Hi sweetie"
  else:
    return "Bye"

print(greeting("frnd"))
