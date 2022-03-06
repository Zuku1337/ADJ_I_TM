import re


def regex_helper(input_str: str, regex_type: str) -> None:
    result = ""
    if regex_type == "numbers":
        result = re.sub('\d', '', input_str)
    elif regex_type == "html":
        result = re.sub('<[^>]*>', '', input_str)
    elif regex_type == "punctuation":
        result = re.sub('[.,;]', '', input_str)
    elif regex_type == "hashtags":
        result = re.findall('#[\w]+', input_str)
    elif regex_type == "emoticons":
        result = re.findall('[:;][^\s]+', input_str)
    print(result)


def main() -> None:
    numbers = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"
    html = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"
    punctuation = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus eu risus."
    hashtags = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus."
    emoticons = "Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."
    regex_helper(numbers, "numbers")
    regex_helper(html, "html")
    regex_helper(punctuation, "punctuation")
    regex_helper(hashtags, "hashtags")
    regex_helper(emoticons, "emoticons")


main()
