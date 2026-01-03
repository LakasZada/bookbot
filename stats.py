def get_num_words(filepath):

    with open(filepath) as f:
        text = f.read()
        return len(text.split())


def count_char(filepath):

    with open(filepath) as f:
        text = f.read()

    counts = {}

    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1

    return counts

    
def char_report(char_counts):
    
    result = []

    for char, count in char_counts.items():
        if char.isalpha():
            result.append({"char":char, "num":count})

    def sort_on(item):
        return item["num"]

    result.sort(reverse=True, key=sort_on)

    return result
    

