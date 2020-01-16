SELECT * FROM "notes" LIMIT 1000;
INSERT INTO notes(title, description, created_date)
VALUES
   ('note 2', 'more descriptions here', now());
