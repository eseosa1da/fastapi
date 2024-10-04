CREATE TABLE "products" (
    name 
)




CREATE TABLE products (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (255) UNIQUE NOT NULL, 
  price bigint NOT NULL
 
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY, 
  title VARCHAR (255)  NOT NULL, 
  content VARCHAR (255)  NOT NULL, 
  published BOOL NOT NULL Default TRUE,
  created_at timestamptz NOT NULL Default NOW()
);


CREATE TABLE votes (
  post_id INT, 
  user_id INT,
  CONSTRAINT post_user_pk PRIMARY KEY (post_id,user_id),
  CONSTRAINT votes_posts_fk FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
  CONSTRAINT votes_users_fk FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


ALTER TABLE posts ADD user_id INT NOT NULL;


INSERT INTO posts (title, content, owner_id) VALUES ('first post', 'some interesting stuff', 11);
INSERT INTO posts (title, content, owner_id) VALUES ('second post', 'some interesting stuff', 13);
INSERT INTO posts (title, content, owner_id) VALUES ('third post', 'some interesting stuff', 13);
INSERT INTO posts (title, content) VALUES ('second post', 'I love posting bro');
INSERT INTO users (email, password) VALUES ('john@gmail.com', 'Bandana7ure');
INSERT INTO products (name, price) VALUES ('microphone', 30);
INSERT INTO products (name, price) VALUES ('Car', 40);


ALTER TABLE posts
ADD CONSTRAINT user_id_fkey
FOREIGN KEY (user_id) REFERENCES users(id);



INSERT INTO votes (post_id, user_id) VALUES (1, 1);
INSERT INTO votes (post_id, user_id) VALUES (3, 4);
INSERT INTO votes (post_id, user_id) VALUES (11, 9);
INSERT INTO votes (post_id, user_id) VALUES (1, 1);
INSERT INTO votes (post_id, user_id) VALUES (20, 1);