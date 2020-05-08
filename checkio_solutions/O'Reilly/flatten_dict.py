#!/usr/bin/env checkio --domain=py run flatten-dict

# 
# END_DESC

def flatten(dictionary):
    # your code here
    new_dict={}
    new_key=''
    def recurse(dictionary,new_key=''):
        for key,value in dictionary.items():
            #new_key = new_key + '/'+ key if new_key else key
            if(isinstance(value,dict)):
                if value:
                    recurse(value,new_key + '/'+ key if new_key else key)
                else:
                    new_dict[new_key + '/'+ key if new_key else key]=""
            else:
                new_dict[new_key + '/'+ key if new_key else key]=dictionary[key]
    recurse(dictionary)
    return new_dict


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')