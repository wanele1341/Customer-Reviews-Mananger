import csv 

class ReviewException(Exception): 
    pass 

file_name = "mr_d_reviews.csv"

def display():
    try:
        with open(file_name , "r")as file:
            reader =  csv.DictReader(file)
            rows = []

            for row in reader:
                try:
                    if not all(row.values()):
                        raise ValueError("Empty field detected!!!")
                    
                    rating  = int(row['rating'])
                    if rating < 1 or rating > 5:
                        raise ValueError("Rating must be between 0 and 5")
                    
                    print(f"ID : {row['review_id']} | Name : {row['customer_name']} | Rating : {row['rating']} | Comment : {row['comment']}")
                    
                    rows.append(row)
                    
                except ValueError as e:
                    print ("Data Error :" , e)


                    with open (file_name , "a" , newline= "")as file:
                        writer = csv.DictWriter(file)

                        writer.writerow([6 , "Ayanda Khumalo" , 4 , " Good Service"])
                        writer.writerow([7, "Zanele Mthembu" , 5 , "Excellent Delivery"])

                        for row in rows:
                            if row['review_id'] == 4:
                                row['rating'] == 3
                                row['comment'] == "Improved delivery time"

                                with open (file_name , "w" , newline="")as file:
                                    fieldnames = ["review_id" , "customer_name" , "rating" , "comment"]
                                    writer = csv.DictWriter(file , fieldnames = fieldnames)

                                    writer.writeheader()
                                    writer.writerows(row)

    except FileNotFoundError as e:
        print("Data Error :" , e)
    except Exception as e:
        print("Unexcpected error!!!:", e)