from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///lenscatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Fake user creation
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Full frame lenses
category1 = Category(name="Full frame", user_id=1)
session.add(category1)
session.commit()

item1 = CategoryItem(name="Canon EF 50mm f/1.8 STM Lens",
                        user_id=1,
                        description="One of the most versatile focal lengths available, the EF 50mm f/1.8 STM Lens from Canon pairs this classic lens design with enhancements to the AF system and physical design that make it both faster and smaller.",
                        price="125.00",
                        picture="https://static.bhphoto.com/images/images500x500/1431316225000_1143786.jpg",
                        category=category1)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Canon EF 24-70mm f/2.8L II USM Lens",
                        user_id=1,
                        description="Spanning a popular and versatile range of focal lengths, the EF 24-70mm f/2.8L II USM is a Canon L-series zoom commonly thought of as the workhorse of lenses.",
                        price="1899.00",
                        picture="https://static.bhphoto.com/images/images500x500/1457983216000_843008.jpg",
                        category=category1)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Canon EF 70-200mm f/2.8L IS II USM Lens",
                        user_id=1,
                        description="A workhorse of a lens, the Canon EF 70-200mm f/2.8L IS II USM is an L-series telephoto zoom characterized by its bright f/2.8 constant maximum aperture and optical image stabilization.",
                        price="2099.00",
                        picture="https://static.bhphoto.com/images/images500x500/1468524687000_680103.jpg",
                        category=category1)
session.add(item3)
session.commit()

# APS-C lenses
category2 = Category(name="APS-C", user_id=1)
session.add(category2)
session.commit()

item1 = CategoryItem(name="Canon EF-S 24mm f/2.8 STM Lens",
                        user_id=1,
                        description="Characterized by a truly thin profile, along with an advanced autofocus motor, the EF-S 24mm f/2.8 STM Lens from Canon is a wide-angle prime designed for APS-C-size EOS DSLRs.",
                        price="149.00",
                        picture="https://static.bhphoto.com/images/images500x500/1464727519000_1081812.jpg",
                        category=category2)
session.add(item1)
session.commit()

item2 = CategoryItem(name="Canon EF-S 10-18mm f/4.5-5.6 IS STM Lens",
                        user_id=1,
                        description="A flexible wide-angle zoom in a compact form factor, the EF-S 10-18mm f/4.5-5.6 IS STM from Canon is a 16-28.8mm equivalent lens designed for EF-S-mount DSLRs.",
                        price="299.00",
                        picture="https://static.bhphoto.com/images/images500x500/1399952762000_1051476.jpg",
                        category=category2)
session.add(item2)
session.commit()

item3 = CategoryItem(name="Canon EF-S 60mm f/2.8 Macro USM Lens",
                        user_id=1,
                        description="Mixing a comfortable short telephoto focal length with optimized close-up capabilities, the EF-S 60mm f/2.8 Macro USM from Canon is an EF-S-mount prime designed for APS-C-format DSLRs.",
                        price="399.00",
                        picture="https://static.bhphoto.com/images/images500x500/1266533223000_371176.jpg",
                        category=category2)
session.add(item3)
session.commit()

print "added lenses!"
