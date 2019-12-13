#Create table -lauseet

```
CREATE TABLE boat (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	boat_type VARCHAR(144) NOT NULL, 
	boat_class VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
```

```
CREATE TABLE reservation (
	id INTEGER NOT NULL, 
	starting_time DATETIME NOT NULL, 
	ending_time DATETIME NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
);
CREATE INDEX ix_reservation_ending_time ON reservation (ending_time);
CREATE INDEX ix_reservation_starting_time ON reservation (starting_time);
```

```
CREATE TABLE boat_reservation (
	reservation_id INTEGER, 
	boat_id INTEGER, 
	FOREIGN KEY(reservation_id) REFERENCES reservation (id), 
	FOREIGN KEY(boat_id) REFERENCES boat (id)
);
CREATE INDEX ix_boat_reservation_reservation_id ON boat_reservation (reservation_id);
```

```
CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
    UNIQUE (name)
);
```

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	email VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
```

```
CREATE TABLE account_role (
	account_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
CREATE INDEX ix_account_role_account_id ON account_role (account_id);
```