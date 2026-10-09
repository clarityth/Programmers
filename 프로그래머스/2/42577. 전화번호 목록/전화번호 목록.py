def solution(phone_book):
    phone_book.sort()
    for i, phone in enumerate(phone_book) :
        if i + 1 < len(phone_book) and phone_book[i+1].startswith(phone) :
            return False
    return True