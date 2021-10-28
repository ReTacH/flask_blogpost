from flask import Flask, g, render_template, current_app
import sqlite3

def getmessage():
  if 'message_db' not in g:
      g.message_db = sqlite3.connect('message_db.sqlite')

  with current_app.open_resource('init.sql') as f:
		g.message_db.executescript(f.read().decode('utf8'))

  return g.message_db

def insert_message(request):
  name = request.form['name']
	message = request.form['message']
	db = get_message_db()
	db.execute(
		'INSERT INTO messages (handle, message) VALUES (?, ?)',
		(name, message)
		)
	db.commit()
	g.pop('message_db', None)
	db.close()


def random_messages(n):
	db = get_message_db()
	msg = db.execute(
		f'SELECT handle, message FROM messages ORDER BY RANDOM() LIMIT {n}'
		).fetchall()

	return msg