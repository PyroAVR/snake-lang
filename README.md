# snake-lang
What is it with all these new-fangled languages anyway?  All their fancy design
rules and pattern-matching.  And what's all this about strong static typing in a
language with garbage collection!  Unthinkable!  Why, the way things are going,
our beloved Python will soon be considered old-world, old-school! Something only
to be used by crusty old data scientists and UNIX sysadmins!  Preposturous!
I propose we move ahead with a modernization of our beloved Python, and show all
these new hot shots that our language can learn their tricks too! I've even
given it a trendy new pseudonym: **snake-lang**

## usage
snake-lang is expressive, beautiful, and simple.  snake-lang was designed with
the programmer in mind, and enforces a strict requirement that the programmer
control over his or her code, and not the other way around.

### get
```
git clone git://github.com/PyroAVR/snake-lang
pip3 install -r snake-lang/requirements.txt
```

Fully compatible with both project-local and system wide installations!

### examples
Using the dynamic class extension ability:
```python
class A(delegates):
    pass


a = A()

@extension(A)
def say_hello(person):
    print("Hello, {0}!".format(person))


a.say_hello('Andy')
# prints "Hello, Andy!"
```
Note that even pre-instantiated objects of type `A` can use the new function!


## features/modules
 - runtime class extensions: "Delegation pattern"
 - subscriber/notifier framework
 - a healthy dose of sarcasm


## seriously?
Listen, it had to be done.  Someone always makes the mistake of asking "can you
do this in Python?" to which the answer is always yes, assuming it required to
be especially performant, and I feel obligated to prove my previous claim.
This is mostly a collection of "what ifs" for sake of showing that it can indeed
be done, regardless of whether it is really a good idea or not.

I don't suggest you use most of this stuff in production at all.  If there are
tests for a module, consider that a bonus more than anything.  Also, I'm sure
none of this is especially performant, though I do try to write things to not
be totally ridiculous in terms of running time.

Hopefully you find this farce as much a comedy as I do :^)
