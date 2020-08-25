My NoSQL User Profile Design
############################

:date: 2020-08-01 10:00
:category: systems
:slug: nosql-user-profile
:authors: Gannon Barnett

In this article I'll review a database design I created for handling user profiles while
prioritizing security and scalability.
Below are the main features I'll review:

- public profile (name, bio, photo …)
- private/secure data (sensitive financial or personal data)


I picked these features because in my original design I found some subtle optimizations
that you might miss during your design phase (like I did). I'll be going over database design,
and stay out of code/ specific tools. But if you're wondering, I used Google Cloud Products.
Specifically I used Firestore (GCP NoSQL database), Firebase Auth and Firebase Storage (large file storage).

Public User Profile
-------------------
Storing a public user profile is fairly straightforward; all attributes of the profile can just be attributes of the user document.



.. image:: {filename}images/messaging_1.png
   :align: center
   :width: 894
   :height: 249



Now let’s add user profile pictures. I integrated Firebase Storage for a large-file storage service. When linking objects from a storage service, it's important to store the file path, and not a URL. This is important for two reasons; first, the access tokens may change and the URL may expire; second, this abstraction allows for easy integration of requesting different sizes of the same image to allow for application scalability and flexibility. With some iPhone images being almost 3mb and 4k pixels, being able to request smaller image sizes can save a substantial amount of download time and storage costs.



.. image:: {filename}images/messaging_2.png
   :width: 200
   :height: 286
   :align: center


With this design, we can resize images by adding a suffix to the original photo id
indicating the file’s scale, and then dynamically generate a filepath.
I could then request the URL for a given filepath and serve it. To implement this
I added a listener to the photos path of my storage bucket which would resize images
when they were added.

Secure User Information
-----------------------
Next, let’s allow for adding secure data. In a NoSQL database, data is loaded each document
at a time so you can't restrict access on specific key/value pairs of a document. Regardless
of what your application retains from document, the entire document is transferred over the network
and cached in the browser, allowing a malicious party to access secure information!


We want different security rules for different parts of the database. To achieve
this we can put different classes of data in different collections.

.. image:: {filename}images/messaging_3.png
   :width: 896
   :height: 494
   :align: center


Now that public and private information are separated, we can selectively expose
only the public information. The private information can still be utilized in the server
context, but it will never be insecurely transferred to the client. Wahoo!

.. image:: {filename}images/messaging_4.png
   :width: 580
   :height: 198
   :align: center


These rules allow secure information to only exist in trusted services. Effectively,
these rules state:
- the user’s document is public
- the user’s ‘secure’ subcollection is never allowed to be read, written, or updated, but data can be accessed by server functions
