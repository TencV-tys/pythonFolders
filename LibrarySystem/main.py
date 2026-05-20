import database as db 

class LibrarySystem:
    def __init__(self,conn):
        self.conn = conn
    
    def addbook(self,title,author):
        return db.add_book(self.conn,title,author)
    
    def show_books(self):
        return db.get_all_books(self.conn)

    def updatebook(self,id,title,author):
        return db.update_book(self.conn,id, title, author)
    
    def deletebook(self,id):
        return db.delete_book(self.conn, id)

    def borrowbook(self,book_id,member_name):
        return db.borrow_book(self.conn,book_id,member_name)
    
    def returnbook(self, book_id):
        return db.return_book(self.conn, book_id)
    
    def showborrowedbooks(self):
        return db.get_borrowed_books(self.conn)

    def bookavailable(self,book_id):
        return db.is_book_available(self.conn, book_id)


try:
    conn = db.setup()
    lb = LibrarySystem(conn)
    while True:
              print("📚 WELCOME TO LIBRARY MANAGER")
              print("1. Add Book")
              print("2. View All Books")
              print("3. Update Book")
              print("4. Delete Book")
              print("5. Borrow Book")
              print("6. Return Book")
              print("7. Show Borrowed Book")
              print("8. Exit")
              
              try:
                choice = int(input('Enter your choice:'))
                if choice == 1:
                    try:
                        title = input("Enter Title: ")
                        author = input("Enter Author:")

                        if not title.strip():
                            raise ValueError("Title cannot be empty")
                        elif not author.strip():
                            raise ValueError("Author need to be filled")
                        
                        lb.addbook(title,author)
                        print(f"book added")
                    except Exception as e:
                        print(f"Unexpected error: {e}")

                elif choice == 2:
                    try:
                         books = lb.show_books()
                         if books:
                            print("All books")
                            for b in books:
                                status = "Borrowed" if not lb.bookavailable(b[0]) else 'Available'
                                print(f"ID:{b[0]} | {b[1]} by {b[2]} | {status}")
                         else:
                            print("No books in library")
                    except Exception as e:
                        print(f"Unexpected error: {e}")
                        
                elif choice == 3:
                    try:
                         books = lb.show_books()
                         if not books:
                            print('No books in library theres nothing to update')
                         else:
                             id = int(input("Enter id: "))
                             title = input("Update Title: ")
                             author = input("Update Author:")
                             if not title.strip():
                               raise ValueError("Title cannot be empty")
                             elif not author.strip():
                               raise ValueError("Author cannot be empty")
                             lb.updatebook(id,title,author)
                             print('Updated successfully')
                    except ValueError as e:
                        printf('Id must be a number')
                    except Exception as e:
                        print(f"Unexpected error: {e}")
                        
                elif choice == 4:
                    try:
                        books = lb.show_books()
                        if not books:
                            print("No books in the library theres nothing to delete")
                        else:
                           id = int(input("Enter id: "))
                           lb.deletebook(id)
                           print('Deleted succesfully')
                    
                    except ValueError as e:
                        print(f"Id must be a number")
                    except Exception as e:
                        print(f"Unexpected error on: {e}")
                elif choice == 5:
                    try:
                      books = lb.show_books()
                      if not books:
                        print("No books in the library")
                      else:
                          book_id = int(input("Enter book id: "))
                          member_name = input("Enter member name: ")
                          if not member_name.strip():
                             raise ValueError("Member name must not be empty")

                          lb.borrowbook(book_id,member_name)
                          print("Borrowed book added")
                    except ValueError as e:
                        print("Book id must be a number")
                    except Exception as e:
                        print("Unexpected error")
                elif choice == 6:
                    try:
                       book_id = int(input('Enter book id:'))
                       lb.returnbook(book_id)
                    except ValueError as e:
                        print(f"book id must be a number")
                    except Exception as e:
                        print("Unexpected error")
                elif choice == 7:
                    try:
                       books = lb.show_books()
                       if not books:
                          print('No books in the library no borrowed happened ')
                       else:
                           borrowed = lb.showborrowedbooks()
                           if borrowed:
                              print("Borrowed Books")
                              for b in borrowed:
                                  print(f"ID: {b[0]} | {b[1]} by {b[2]} | Borrowed by: {b[3]} | Date: {b[4]}")
                           else:
                              print("No book borrowed")

                    except Exception as e:
                        print("Unexpecetd error")
                else:
                    try:
                        print("Exiting...")
                        conn.close()
                        break
                    except:
                        pass

              except ValueError as e:
                print("Select only a number")
              except Exception as e:
                print(f"Unexpected Error: {e}")          

except Exception as e:
    print(f'Unexpected error:{e}')
finally:
    try:
       if conn:
          conn.close()
          print("Database connection close")
    except:
        pass
