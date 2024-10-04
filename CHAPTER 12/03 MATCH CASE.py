def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal servr error"
        case _:
            return "Unknown Status"
        

#usages 
print(http_status(200)) # Output: OK print(http_status(404))  
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(456)) # Output: Unknown status