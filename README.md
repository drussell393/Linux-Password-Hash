# Linux Password Hash (written in Python)

The idea behind this script is to allow for system administrators to hash people's passwords
without giving them access to the server they need the password on. 

I've seen some scary techniques in the past, including but not limited to:

- Giving out passwords
- Giving someone access to a Linux box to type the password
- Making temp passwords and then sending em via e-mail or PostIt

This essentially diminishes those techniques, because while we are letting that other person
type their password using getpass(), we're never seeing the password (as a Linux Sys Admin),
and we're just getting the final SHA-512 hash, with a random Salt.

This will be a limited use case, because it's designed to be used for SSH/e-mail passwords,
assuming you use Linux user auth for your e-mail server (most MTAs support this). However,
it is used quite often in the groups I'm in so, here's to releasing this quick script.

As always, questions/comments are appreciated.

Much Love,

Dave.

## Using the Sucker

Pretty easy. If you're running on a Linux system, just use `chmod +x passwordhasher.py` to make
the file executable, and then run `./passwordhasher.py`. It will ask for a password, and then a
confirmation password. Assuming you get everything right, it will spit out a hash ready for usage
in your `/etc/shadow` file.

I may have added some neat quotes too. You're welcome.
