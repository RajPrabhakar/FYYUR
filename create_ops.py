import sys

from models import (
  app,
  db,
  Venue,
  Artist,
  Show
)
from forms import *
from flask import (
  render_template,
  request,
  flash
)

#  Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  form = VenueForm(request.form)
  error = False

  try:
    venue = Venue()
    if form.validate():
      form.populate_obj(venue)
      db.session.add(venue)
      db.session.commit()
    else:
      error=True
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()

  # on successful db insert, flash success
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  if not error:
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
  else:
    flash('Uh-Oh')

  return render_template('pages/home.html')

#  Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  form = ArtistForm(request.form)
  error = False

  try:
    artist = Artist()
    if form.validate():
      form.populate_obj(artist)
      db.session.add(artist)
      db.session.commit()
    else:
      error = True
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()

  # on successful db insert, flash success
  if not error:
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  else:
    flash('Uh-Oh')
  return render_template('pages/home.html')

#  Show
#  ----------------------------------------------------------------

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  form = ShowForm(request.form)
  error = False

  try:
    show = Show()
    if form.validate():
      form.populate_obj(show)
      db.session.add(show)
      db.session.commit()
    else:
      error = True
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()

  # on successful db insert, flash success
  if not error:
    flash('Show was successfully listed!')
  else:
    flash('Uh-Oh')
  return render_template('pages/home.html')