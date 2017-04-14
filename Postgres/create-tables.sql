CREATE TABLE public.users
(
    id serial NOT NULL,
    screen_name character varying(255),
    oauth_token character varying(255),
    oauth_token_secret character varying(255),
    CONSTRAINT users_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;
