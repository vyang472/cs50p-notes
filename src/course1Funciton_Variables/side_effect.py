sentence = "you know I'm say"

def main():
    global sentence
    say("you are a good guy")
    sentence = "you know"
    say("really")



def say(phrase):
    print(phrase+" "+sentence)

main()