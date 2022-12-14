import re
import random



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'Yo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'are', 'you'])
    response('Perfectly fine', ['how', 'is', 'your', 'day'], required_words=['how', 'day'])
    response('Robo', ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
    response('My pleasure..', ['thank you', 'thanks'], single_response=True)
    response('You don\'t have to say that!!!Anyway,Thank you!', ['you', 'are', 'nice'], required_words=['you', 'nice'])
    response('Thanks!', ['you', 'are', 'sweet'], required_words=['you', 'sweet'])
    response('I am a bot my origin is processor!!!',['where','are','you','from'] , required_words=['where', 'you', 'from'])
    response('I am as old as the website', ['how', 'old', 'are', 'you'], required_words=['how', 'old'])
    response('My age is the same as the website', ['what', 'is', 'your', 'age'], required_words=['your', 'age'])
    response('I do not have any favourite color', ['your', 'color'], required_words=['color'])
    response('Go to the search box please', ['Where', 'is', 'internet'], required_words=['internet'])
    response('Go to the query button!!Thank you!', ['I', 'have', 'a question'], required_words=['Qusetion'])



    def unknown():
        response = ["Could you please re-write that on query-box? ",
                    "Sorry!!I may help you from the query-box",
                    "I can help you through the query-box",
                    "please go to the query-box"][
            random.randrange(4)]
        return response




    # Longer responses
    R_EATING = "I don't like eating anything because I'm a bot obviously!"
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system

print(get_response(input('')))