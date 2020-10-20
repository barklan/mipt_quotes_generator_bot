import vkapi
import markovify
from settings import vktoken, target_id


def cleaner(posts):
    cleaned_posts = posts.copy()

    '''
    Remove non-quote posts (usually long posts) and Dialog qoutes:
    'П: Здравствуйте, вы меня слышите? \nС: Да\nП: Жаль. Значит придётся провести семинар. \n\n#Тумайкин_mipt'
    '''

    for post in cleaned_posts:
        if (len(post) > 200):
            cleaned_posts.remove(post)

    for post in cleaned_posts:
        if (':' in post):
            cleaned_posts.remove(post)


    '''
    TODO
    'Гомоморфный образ группы,\nБудь во имя коммунизма\nИзоморфен фактор-группе\nПо ядру гомоморфизма!\n\n#Богданов_mipt'

    '*семинар по мат.анализу*\nРебята, я даже не знаю как вам прорекламировать этот ужас. Терпите, терпите... \n\n#Дымарский_mipt'

    '''


    '''
    TODO
    Ideal qoute (to split by '#', select first, remove newline characters):
    'Это нельзя не решить, это статья уже\n\n#Бурмистров_mipt'
    '''
    for i in range(len(cleaned_posts)):
        segmentlist = list(map(str, cleaned_posts[i].split('#')))
        post = segmentlist[0]
        post = post[:-1]
        cleaned_posts[i] = post


    return cleaned_posts

        
def write_list_to_file(posts):

    '''
    Writes list of strings into file - each string on it's own line
    to subsequently use markovify.NewlineText class instead of markovify.Text

    TODO
    Need to make a permanent file to add quotes to
    and write a function that adds to this file only non-existent quotes form newly got ones
    '''

    with open('corpus.txt', 'w', encoding='utf8') as file:
        file.writelines(posts)


def fit_model():
    
    posts = vkapi.get_wall_posts(vktoken, target_id)
    posts = cleaner(posts)
    write_list_to_file(posts)
    
    # Get raw text as string.
    with open("corpus.txt", encoding='utf8') as file:
        text = file.read()

    # Build the model.
    text_model = markovify.NewlineText(text, state_size=1)

    return text_model


def get_quote(model):
    return model.make_sentence()

