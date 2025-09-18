CREATE TABLE public.allpasswds
(
    id bigserial NOT NULL,
    platform text NOT NULL,
    passwd text NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.allpasswds
    OWNER to postgres;