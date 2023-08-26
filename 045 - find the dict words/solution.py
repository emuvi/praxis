
def back_tracking():

    def find_sentence(dictionary, s):
        sentence, valid = find_sentence_helper(dictionary, s)
        if valid:
            return sentence


    def find_sentence_helper(dictionary, s):
        if len(s) == 0:
            return [], True

        result = []
        for i in range(len(s) + 1):
            prefix, suffix = s[:i], s[i:]
            if prefix in dictionary:
                rest, valid = find_sentence_helper(dictionary, suffix)
                if valid:
                    return [prefix] + rest, True
        return [], False
    

def dynamic_programming():

    def find_sentence(s, dictionary):
        starts = {0: ''}
        for i in range(len(s) + 1):
            new_starts = starts.copy()
            for start_index, _ in starts.items():
                word = s[start_index:i]
                if word in dictionary:
                    new_starts[i] = word
            starts = new_starts.copy()

        result = []
        current_length = len(s)
        if current_length not in starts:
            return None
        while current_length > 0:
            word = starts[current_length]
            current_length -= len(word)
            result.append(word)

        return list(reversed(result))