{% include base.html %}

# Week-2

  
## 5.5 Legal and Ethical Concerns
When you create a GitHub repository it requests a license type. Review the license types in relationship to this Tech Talk and make some notes in GitHub pages.

Make a license for your personal and Team project. Document license you picked and why.
- For personal, I chose the unlicense license because it is the most 'free', in the sense that it allows the most freedom for other people to use on their own in hopes of better understanding.
- For the Team project, we chose the MIT license. I believe some of us have used this license beforehand and we like to assume it is the default. It also provides a lot of leniency and freedom including usage and distribution without credit. However, it does state that the original holders would be liable for any problems that come from copying it.

## 5.6 Safe Computing
Describe PII you have seen on project in CompSci Principles.
- Last trimester, we had our name, email, and phone numbers in a database as a default testing system for CRUD. These are all personally identifiable information.

What are your feelings about PII and your exposure?
- I think while it is not necessarily a bad thing, having too much information about you out there is definitely dangerous.

Describe good and bad passwords? What is another step that is used to assist in authentication.
- Most good passwords are longer strings of both letters, numbers, and special characters with no set pattern or rythmn so it cannot be brute forced or easily guessed. Other services provide 2FA (2 factor authentication) to ensure greater security.
  
Try to describe Symmetric and Asymmetric encryption.
- Syymmetric = One key is used to both encrypt and decrypt between both sides
- Asymmetric = Both a public and private key is utilized for everyone to ensure greater security.

Provide and example of encryption we used in deployment.
- For deployment, we used certbot to get an SSL certificate, which allows to go from http --> https. 

Describe a phishing scheme you have learned about the hard way. Describe some other phishing techniques.
- Email phishing is quite common. Although I have not fallen for it yet, a lot of emails get redirected to our spam/junk emails which often try to ask for personal infromation.
- Some people also do spear phishing to make their phishes look more realistic, often providing more publicly available information about their target to try and decieve them into thinking it is a legitimate email.