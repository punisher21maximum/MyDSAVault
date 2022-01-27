
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        asciiOfA = ord('a')
        asciiOfCh = ord(ch)
        return asciiOfCh - asciiOfA

    def insert(self, word):
        currNode = self.root

        for idxOfChInWord in range(len(word)):
            idxOfAlpha = self.charToIndex(word[idxOfChInWord])

            if not currNode.children[idxOfAlpha]:
                currNode.children[idxOfAlpha] = TrieNode()
            currNode = currNode.children[idxOfAlpha]

        currNode.isEndOfWord = True

    def search(self, word):
        currNode = self.root

        for idxOfChInWord in range(len(word)):
            alpha = word[idxOfChInWord]
            idxOfAlpha = self.charToIndex(alpha)
            print(currNode.children)
            if currNode.children[idxOfAlpha] is None:
                break
            currNode = currNode.children[idxOfAlpha]

        if currNode.isEndOfWord:
            print('Found')
        else:
            print('Not Found')

    def deleteWord(self, word):

        pass

    def printTrie(self, currNode):
        currNode = self.root

        if currNode.isEndOfWord:
            return
        else:
            for i in range(len(currNode.children)):
                node = currNode.children[i]
                if node:
                    print(chr(i))
                    self.printTrie(node)


t = Trie()
keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
for key in keys:
    t.insert(key)

# keys = ["theeadsad", "a", "there", "anaswe", "any", "by", "their"]
# for key in ["there"]:
#     t.search(key)

t.printTrie(t.root)
