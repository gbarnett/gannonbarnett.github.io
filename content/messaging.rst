My NoSQL User Profile Design
############################

:date: 2020-08-01 10:00
:category: systems
:slug: nosql-user-profile
:authors: Gannon Barnett

In this article I'll review a database design I created for handling user profiles while prioritizing security and scalability.
Below are the main features I'll review:

- public profile (name, bio, photo …)
- private/secure data (credit card number, home address … )


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


With this design, we can resize images by adding a suffix to the original photo id indicating the file’s scale, and then dynamically generate a filepath. I could then request the URL for a given filepath and serve it. To implement this I added a listener to the photos path of my storage bucket which would resize images when they were added.

Secure User Information
-----------------------
Next, let’s allow for adding secure data. In a NoSQL database, data is loaded each document at a time so you can't restrict access on specific key/value pairs of a document. Regardless of what your application keeps from the document the entire document is transferred over the network, allowing malicious hackers to potentially steal some supposedly private information! To prevent sending secure information to an untrusted client, we can move all actions with secure information to server-side, and add an API interface for the client. To allow for public access of the user profile and restricted access of secure information, we can seperate the secure information into a nested collection. I implemented the follow design (note that this design has the implicit assumption that the base user document is public, and only explicitly specifies the documents in the secure collection as secure).


.. image:: {filename}images/messaging_3.png
   :width: 896
   :height: 494
   :align: center



We can then configure our database security rules so our public user profile is accessible and our secure user information is not.

.. image:: {filename}images/messaging_4.png
   :width: 580
   :height: 198
   :align: center


These rules enforce the following security restrictions:
only the user may edit their own information

- the user’s document is public
- the user’s ‘secure’ subcollection is never allowed to be read, written, or updated (default behavior is no access, rules only act on the specific path)
