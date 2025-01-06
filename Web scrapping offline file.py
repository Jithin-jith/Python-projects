from bs4 import BeautifulSoup

with open('index.html','r') as file:
    doc = BeautifulSoup(file,'html.parser')
    
#print(doc.prettify())

title_tag = doc.title.string
print(f'Title is :  {title_tag}')

doc.title.string = 'COOKING'
print(f'New Title is :  {doc.title.string}')

#find the first paragraph
para1 = doc.find('p').string
print(f'First paragraph is : {para1}')

#find all the paragraphs
paras = doc.find_all('p')
print(f'Type of paras is : {type(paras)}')
print(f'Number of paragraphs is : {len(paras)}')

print('The following are the paragrapghs in the webpage: ')
for i in range(len(paras)):
    print(f'Paragraph {i} : {paras[i].string}')
