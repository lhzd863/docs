CREATE TABLE calendar
(
  calendar_date date,
  day_of_week integer,
  day_of_month integer,
  day_of_year integer,
  day_of_calendar integer,
  weekday_of_month integer,
  week_of_month integer,
  week_of_year integer,
  week_of_calendar integer,
  month_of_quarter integer,
  month_of_year integer,
  month_of_calendar integer,
  quarter_of_year integer,
  quarter_of_calendar integer,
  year_of_calendar integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE calendar
  OWNER TO petl;

CREATE TABLE calendar
(
  calendar_date date,
  day_of_week integer,
  day_of_month integer,
  day_of_year integer,
  day_of_calendar integer,
  weekday_of_month integer,
  week_of_month integer,
  week_of_year integer,
  week_of_calendar integer,
  month_of_quarter integer,
  month_of_year integer,
  month_of_calendar integer,
  quarter_of_year integer,
  quarter_of_calendar integer,
  year_of_calendar integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE calendar
  OWNER TO petl;


CREATE TABLE datacalendaryear
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  calendaryear integer NOT NULL,
  CONSTRAINT datacalendaryear_pkey PRIMARY KEY (etl_system, etl_job, calendaryear)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE datacalendaryear
  OWNER TO petl;

CREATE TABLE etl_event
(
  eventid character varying(20) NOT NULL,
  eventstatus character(1) NOT NULL,
  severity character(1) NOT NULL,
  description character varying(200),
  logtime character(19) NOT NULL,
  closetime character(19)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_event
  OWNER TO petl;

CREATE TABLE etl_groupmember
(
  username character varying(15) NOT NULL,
  groupname character varying(15) NOT NULL,
  CONSTRAINT etl_groupmember_pkey PRIMARY KEY (username, groupname)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_groupmember
  OWNER TO petl;

CREATE TABLE etl_job
(
  etl_system character varying(30),
  etl_job character varying(80),
  etl_server character varying(10),
  description character varying(80),
  frequency character varying(30),
  jobtype character(1),
  enable character(1),
  last_starttime character(19),
  last_endtime character(19),
  last_jobstatus character varying(20),
  last_txdate date,
  last_filecnt integer,
  last_cubestatus character(20),
  cubeflag character(1),
  checkflag character(1),
  autooff character(1),
  checkcalendar character(1),
  calendarbu character varying(15),
  runningscript character varying(80),
  jobsessionid integer,
  expectedrecord integer,
  checklaststatus character(1),
  timetrigger character(1),
  job_priority integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job
  OWNER TO petl;

CREATE TABLE etl_job_dependency
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  dependency_system character varying(30) NOT NULL,
  dependency_job character varying(80) NOT NULL,
  description character varying(80),
  enable character(1),
  dep_mode character(1) NOT NULL DEFAULT '0'::bpchar,
  CONSTRAINT etl_job_dependency_pkey PRIMARY KEY (etl_system, etl_job, dependency_system, dependency_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_dependency
  OWNER TO petl;

CREATE TABLE etl_job_group
(
  groupname character varying(80) NOT NULL,
  description character varying(80),
  etl_system character varying(30),
  etl_job character varying(80),
  autoonchild character(1),
  CONSTRAINT etl_job_group_pkey PRIMARY KEY (groupname)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_group
  OWNER TO petl;

CREATE TABLE etl_job_groupchild
(
  groupname character varying(80) NOT NULL,
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  description character varying(80),
  enable character(1),
  checkflag character(1),
  txdate character(10),
  turnonflag character(1),
  CONSTRAINT etl_job_groupchild_pkey PRIMARY KEY (groupname, etl_system, etl_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_groupchild
  OWNER TO petl;

CREATE TABLE etl_job_log
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  jobsessionid integer NOT NULL,
  scriptfile character varying(60) NOT NULL,
  txdate date NOT NULL,
  starttime character(19),
  endtime character(19),
  returncode integer,
  seconds integer,
  logcontent bytea,
  step_no smallint
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_log
  OWNER TO petl;

CREATE TABLE etl_job_logcontent
(
  tx_date date NOT NULL,
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  jobsessionid integer NOT NULL,
  step_no smallint NOT NULL,
  seq_no smallint NOT NULL,
  log_info text,
  CONSTRAINT etl_job_logcontent_pkey PRIMARY KEY (etl_system, etl_job, jobsessionid, step_no)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_logcontent
  OWNER TO petl;

CREATE TABLE etl_job_queue
(
  etl_server character varying(10) NOT NULL,
  seqid integer NOT NULL,
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  txdate date NOT NULL,
  requesttime character varying(19) NOT NULL
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_queue
  OWNER TO petl;

CREATE TABLE etl_job_source
(
  source character varying(50),
  etl_system character varying(30),
  etl_job character varying(80),
  conv_file_head character varying(80),
  autofilter character(1),
  alert character(1),
  beforehour integer,
  beforemin integer,
  offsetday integer,
  lastcount integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_source
  OWNER TO petl;

CREATE TABLE etl_job_status
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  jobsessionid integer NOT NULL,
  txdate date NOT NULL,
  starttime character(19),
  endtime character(19),
  jobstatus character varying(20),
  filecnt integer,
  cubestatus character varying(20),
  expectedrecord integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_status
  OWNER TO petl;

CREATE TABLE etl_job_step
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  step_no smallint NOT NULL,
  step_type character(1) NOT NULL,
  osprogram character varying(80) NOT NULL,
  workdir character varying(64),
  scriptname character varying(80),
  scriptpath character varying(500),
  additionparameters character varying(500),
  description character varying(80),
  enable character(1) DEFAULT '1'::bpchar,
  CONSTRAINT etl_job_step_pkey PRIMARY KEY (etl_system, etl_job, step_no)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_step
  OWNER TO petl;

CREATE TABLE etl_job_stream
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  stream_system character varying(30) NOT NULL,
  stream_job character varying(80) NOT NULL,
  description character varying(80),
  enable character(1),
  CONSTRAINT etl_job_stream_pkey PRIMARY KEY (etl_system, etl_job, stream_system, stream_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_stream
  OWNER TO petl;

CREATE TABLE etl_job_timewindow
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  allow character(1) NOT NULL,
  beginhour integer NOT NULL,
  endhour integer NOT NULL,
  CONSTRAINT etl_job_timewindow_pkey PRIMARY KEY (etl_system, etl_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_timewindow
  OWNER TO petl;

CREATE TABLE etl_job_trace
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  txdate date NOT NULL,
  jobstatus character varying(20),
  starttime character(19),
  endtime character(19),
  CONSTRAINT etl_job_trace_pkey PRIMARY KEY (etl_system, etl_job, txdate)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_job_trace
  OWNER TO petl;

CREATE TABLE etl_locks
(
  etl_server character varying(10) NOT NULL,
  start_time timestamp(0) without time zone NOT NULL DEFAULT ('now'::text)::timestamp(0) with time zone,
  heartbeat timestamp(0) without time zone NOT NULL DEFAULT ('now'::text)::timestamp(0) with time zone,
  jobcount smallint NOT NULL,
  CONSTRAINT etl_locks_pkey PRIMARY KEY (etl_server)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_locks
  OWNER TO petl;

CREATE TABLE etl_notification
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  seqid integer NOT NULL,
  desttype character(1),
  groupname character varying(15),
  username character varying(15),
  timing character(1),
  attachlog character(1),
  email character(1),
  shortmessage character(1),
  messagesubject character varying(160),
  messagecontent character varying(255)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_notification
  OWNER TO petl;

CREATE TABLE etl_received_file
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  jobsessionid integer NOT NULL,
  receivedfile character varying(80) NOT NULL,
  filesize numeric(18,0),
  expectedrecord integer,
  arrivaltime character(19),
  receivedtime character(19),
  location character varying(128),
  status character(1),
  CONSTRAINT etl_received_file_pkey PRIMARY KEY (etl_system, etl_job, receivedfile)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_received_file
  OWNER TO petl;

CREATE TABLE etl_record_log
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  jobsessionid integer NOT NULL,
  recordtime character(19),
  insertedrecord integer,
  updatedrecord integer,
  deletedrecord integer,
  duplicaterecord integer,
  outputrecord integer,
  etrecord integer,
  uvrecord integer,
  er1record integer,
  er2record integer,
  CONSTRAINT etl_record_log_pkey PRIMARY KEY (etl_system, etl_job, jobsessionid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_record_log
  OWNER TO petl;

CREATE TABLE etl_relatedjob
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  relatedsystem character varying(30) NOT NULL,
  relatedjob character varying(80) NOT NULL,
  checkmode character(1),
  description character varying(80),
  CONSTRAINT etl_relatedjob_pkey PRIMARY KEY (etl_system, etl_job, relatedsystem, relatedjob)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_relatedjob
  OWNER TO petl;

CREATE TABLE etl_server
(
  etl_server character varying(10) NOT NULL,
  description character varying(80),
  ipaddress character varying(15),
  agentport integer,
  livecount integer,
  isprimary character(1) NOT NULL DEFAULT 'N'::bpchar,
  issmssend character(1) NOT NULL DEFAULT 'N'::bpchar,
  langcharset character varying(20) NOT NULL DEFAULT 'GB18030'::character varying,
  lastruntime smallint NOT NULL DEFAULT 0,
  lastrundate date NOT NULL DEFAULT ('now'::text)::date,
  CONSTRAINT etl_server_pkey PRIMARY KEY (etl_server)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_server
  OWNER TO petl;

CREATE TABLE etl_sys
(
  etl_system character varying(30) NOT NULL,
  description character varying(80),
  datakeepperiod integer,
  logkeepperiod integer,
  recordkeepperiod integer,
  CONSTRAINT etl_sys_pkey PRIMARY KEY (etl_system)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_sys
  OWNER TO petl;

CREATE TABLE etl_timetrigger
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  triggertype character(1) NOT NULL,
  starthour integer NOT NULL,
  startmin integer NOT NULL,
  offsetday integer NOT NULL,
  CONSTRAINT etl_timetrigger_pkey PRIMARY KEY (etl_system, etl_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_timetrigger
  OWNER TO petl;

CREATE TABLE etl_timetrigger_calendar
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  seq integer NOT NULL,
  yearnum integer,
  monthnum integer,
  daynum integer,
  CONSTRAINT etl_timetrigger_calendar_pkey PRIMARY KEY (etl_system, etl_job, seq)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_timetrigger_calendar
  OWNER TO petl;

CREATE TABLE etl_timetrigger_monthly
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  timing character(31) NOT NULL,
  endofmonth character(1) NOT NULL,
  CONSTRAINT etl_timetrigger_monthly_pkey PRIMARY KEY (etl_system, etl_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_timetrigger_monthly
  OWNER TO petl;

CREATE TABLE etl_timetrigger_weekly
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  timing character(7) NOT NULL,
  CONSTRAINT etl_timetrigger_weekly_pkey PRIMARY KEY (etl_system, etl_job)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_timetrigger_weekly
  OWNER TO petl;

CREATE TABLE etl_user
(
  username character varying(15) NOT NULL,
  description character varying(80),
  email character varying(80),
  mobile character varying(20),
  status character(1),
  CONSTRAINT etl_user_pkey PRIMARY KEY (username)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_user
  OWNER TO petl;

CREATE TABLE etl_user_rights
(
  username character varying(15),
  etl_system character varying(4),
  etl_rights character(1)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_user_rights
  OWNER TO petl;
CREATE TABLE etl_usergroup
(
  groupname character varying(15) NOT NULL,
  description character varying(80),
  CONSTRAINT etl_usergroup_pkey PRIMARY KEY (groupname)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE etl_usergroup
  OWNER TO petl;

CREATE TABLE job_log
(
  etl_system character varying(30) NOT NULL,
  etl_job character varying(80) NOT NULL,
  jobsessionid integer NOT NULL,
  scriptfile character varying(60) NOT NULL,
  txdate date NOT NULL,
  starttime character(19),
  endtime character(19),
  returncode integer,
  seconds integer,
  logcontent text,
  step_no smallint
)
WITH (
  OIDS=FALSE
);
ALTER TABLE job_log
  OWNER TO petl;
