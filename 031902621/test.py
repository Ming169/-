from main import *

if __name__ == '__main__':
    word = ['狐臭', 'shit', '你好']
    org = [
        '小说狐^^chou是以刻hc画人物s**hit形象为中心，通过完你^^女子整的故事情节和环境描写来反映社会生活的文学体裁。',
        '小说刻画虎^^抽人物s&hit的方法：心理n%h描写、动作描写、语言描写、外貌描写'
    ]
    test_ans = ['狐^^chou', 'hc', 's**hit', '你^^女子', '虎^^抽', 's&hit', 'n%h']
    ans = []
    dfa = DFAUtils()
    dfa.word = word
    dfa.org = org
    dfa.write_mes()
    # ans.append(flat(dfa.get_match_word(i)[0]))
    for i in org:
        ans.append(dfa.get_match_word(i)[0])
    assert test_ans == flat(ans)
