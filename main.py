

if __name__ == "__main__":
    
    text_file = open("test.txt", "r")
    main_string = text_file.read().replace('\n', '')
    text_file.close()
    

    print(main_string)


