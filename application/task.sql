/*---------------------------------------------
    TABLE CREATION
---------------------------------------------*/

CREATE TABLE IF NOT EXISTS useraccess (
    useraccess_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    acceshash VARCHAR(32),
    fecha_registro DATE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS task (
    task_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(32),
    description VARCHAR(32),
    done BOOL,
    useraccess INT(11),
    FOREIGN KEY (useraccess)
        REFERENCES useraccess (useraccess_id)
        ON DELETE SET NULL
) ENGINE=InnoDB;


#DUMMY DATA TO PREFILL TABLE
INSERT INTO task(title, description, done) VALUES ('room', '374', FALSE);
INSERT INTO task(title, description, done) VALUES ('room', '312', TRUE);
INSERT INTO task(title, description, done) VALUES ('room', '112', TRUE);