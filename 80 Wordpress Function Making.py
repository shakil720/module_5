import wp_function



first_paragraph_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

heading_one = "Why do we use it?"
second_paragraph_text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."


article = wp_function.wp_paragraph(first_paragraph_text)+wp_function.wp_h2(heading_one)+wp_function.wp_paragraph(second_paragraph_text)


print(article)



