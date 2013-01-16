ALTER TABLE images_image RENAME TO temp_images_image;
CREATE TABLE "images_image" (
    "id" integer NOT NULL PRIMARY KEY,
    "image" varchar(100) NOT NULL,
    "name" varchar(150) NOT NULL UNIQUE,
    "pmhid" varchar(40) NOT NULL,
    "included" bool NOT NULL,
    "alt_text" text NOT NULL,
    "caption" text NOT NULL,
    "pmh_caption" text NOT NULL,
    "source_url" varchar(200) NOT NULL,
    "orig_figure_source" text NOT NULL,
    "pmh_figure_source" text NOT NULL,
    "name_of_source" varchar(50) NOT NULL,
    "blob" text NOT NULL,
    "related_terms" text NOT NULL
);
INSERT INTO images_image (id, image, name, pmhid, included, alt_text, caption, pmh_caption, source_url, orig_figure_source, pmh_figure_source, name_of_source, blob, related_terms) SELECT id, image, name, pmhid, included, alt_text, caption, '', source_url, orig_figure_source, pmh_figure_source, name_of_source, blob, related_terms FROM temp_images_image;
DROP TABLE IF EXISTS temp_images_image;

.mode col
.headers on
select name, caption, pmh_caption from images_image where id=1;
