from models import Venue, app, db
from flask import flash, request, render_template

#  Venue
#  ----------------------------------------------------------------

@app.route('/venues/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None
#   error = False
#   try:
#     Venue.query.get(venue_id).delete()
#     db.session.commit()
#   except:
#     error = True
#     db.session.rollback()
#   finally:
#     db.session.close()

#   if not error:
#     flash('Venue ' + request.form['name'] + ' was successfully updated!')
#   else:
#     flash('Uh-Oh')
#   return render_template('pages/home.html')

#  Artist
#  ----------------------------------------------------------------



#  Show
#  ----------------------------------------------------------------