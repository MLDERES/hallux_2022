from mimesis import Person, Text, Datetime, Internet
from mimesis.enums import Gender, FileType, MimeType

# Let's start by generating a person
p = Person()

print(f'Meet {p.full_name()}, they are a(n) {p.occupation()} '
        f'from {p.university()}')

# Now some random text strings
t = Text()

print(f'{t.quote()}')
print(f'{t.words(5)}')