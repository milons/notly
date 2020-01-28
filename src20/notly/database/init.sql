-- Prepare tables

CREATE TABLE "epoches" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"href"	TEXT NOT NULL,
	"main_image"	TEXT,
	"description"	TEXT,
	"full_description"	TEXT
);

CREATE TABLE "artists" (
	"id"	INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"href"	TEXT NOT NULL,
	"epoch_id"	INTEGER NOT NULL,
	"description"	TEXT,
	"main_image"	TEXT
);


-- Fill with demo data

INSERT INTO "main"."epoches" ("id", "name", "href", "main_image", "description") VALUES ('1', 'Medieval', 'medieval', 'medieval_music_thumb.jpg', 'Medieval music consists of songs, instrumental pieces, and liturgical music from about 500 A.D. to 1400. Medieval music was an era of Western music, including liturgical music...');
INSERT INTO "main"."epoches" ("id", "name", "href", "main_image", "description") VALUES ('2', 'Renaissance', 'renaissance', 'renaissance_music_thumb.jpg', 'Renaissance music is vocal and instrumental music written and performed in Europe during the Renaissance era. Consensus among music historians has been to start the era around 1400, with the end of the medieval era, and to close it around 1600, with the beginning of the Baroque period...');
INSERT INTO "main"."epoches" ("id", "name", "href", "main_image", "description") VALUES ('3', 'Baroque', 'baroque', 'baroque_music_thumb.jpg', 'Baroque music is a period or style of Western art music composed from approximately 1600 to 1750.[1] This era followed the Renaissance music era, and was followed in turn by the Classical era...');
INSERT INTO "main"."epoches" ("id", "name", "href", "main_image", "description") VALUES ('4', 'Classical period', 'classical', 'classical_music_thumb.jpg', 'The Classical period was an era of classical music between roughly 1730 and 1820. The Classical period falls between the Baroque and the Romantic periods...');
INSERT INTO "main"."epoches" ("id", "name", "href", "main_image", "description") VALUES ('5', 'Romantic', 'romantic', 'romantic_music_thumb.jpg', 'Romantic music is a stylistic movement in Western classical music associated with the period spanning the nineteenth century, commonly referred to as the Romantic era...');