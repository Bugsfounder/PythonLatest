name = "bugs"
date = "19-jun-2024"

letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
