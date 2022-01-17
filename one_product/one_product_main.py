import csv

from one_product.one_product_functions import extract_one_book, validate_url, format_text, extract_cover_choice


END_MESSAGE = "INFORMATION: End of extraction"


def one_book(labels, path_to_extract_one_product):
    """Instruction suite for extracting data from a single book.

                Args:
                    labels (list): Column headers of csv files.
                    path_to_extract_one_product (WindowsPath): Path to extract the book.

                """
    # type a correct url
    url = validate_url()

    # Extract cover True or False
    cover = extract_cover_choice()

    # Extract data
    datas = extract_one_book(book_url=url, cover=cover, img_path=path_to_extract_one_product)

    # Format title
    title = datas["title"]
    formatted_title = format_text(string_to_format=title)
    file_name = f"{formatted_title}_extract"

    # save data to csv file
    with open(file=f'{path_to_extract_one_product}/{file_name}.csv',
              mode='w',
              encoding="utf-8",
              newline="") as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        writer.writerow(datas)

    print(f"END_MESSAGE -> {datas['title']}")
