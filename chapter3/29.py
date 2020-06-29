import json
import gzip
import re
import urllib.parse, urllib.request

def get_UK_text():
    with gzip.open("jawiki-country.json.gz") as f:
        for line in f:
            data = json.loads(line)
            if data["title"] == "イギリス":
                return data["text"]

def remove_markup_and_link(target):
    pattern = re.compile(r'''
                        (\'{2,5})
                        (.*?)
                        (\1)
                        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\2', target)
    
    pattern = re.compile(r'''
                            \[\[
                            (?:
                                [^|]*?
                                \|
                            )*?
                            ([^|]*?)
                            \]\]
                        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)
    
    pattern = re.compile(r'''
                        \{\{lang
                        (?:
                            [^|]*?
                            \|
                        )*?
                        ([^|]*?)
                        \}\}
                        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)
    
    pattern = re.compile(r'''
                        \[http:\/\/
                        (?:
                            [^\s]*?
                            \s
                        )?
                        ([^]]*?)
                        \]
                        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)
    
    pattern = re.compile(r'''
                        <
                        \/?
                        [br|ref]
                        [^>]*?
                        >
                        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub('', target)
    
    pattern = re.compile(r'^(\[\[|\{\{)')
    target = pattern.sub('', target)
    
    return target

if __name__ == "__main__":
    pattern = re.compile("^\{\{基礎情報.*?$(.*?)^\}\}$", re.MULTILINE + re.DOTALL)
    contents = pattern.findall(get_UK_text())
    
    pattern = re.compile("""^\|
                            (.*?)
                            \s*
                            =
                            \s*
                            (.+?)
                            (?:
                                (?=\n\|)    # 改行 + '|' の手前(肯定の先読み)
                                | (?=\n$)   # または、改行 + 終端の手前(肯定の先読み)
                            )
                        """, re.MULTILINE + re.VERBOSE + re.DOTALL)
    fields = pattern.findall(contents[0])
    
    result = {}
    for field in fields:
        result[field[0]] = remove_markup_and_link(field[1])
        
    fname_flag = result['国旗画像']
    
    url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'
    
    request = urllib.request.Request(url,
        headers={'User-Agent': 'NLP100_Python(@hogehoge)'})
    connection = urllib.request.urlopen(request)
    
    data = json.loads(connection.read().decode())
    
    url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    print(url)