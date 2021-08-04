/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     29.06.2021 16:33:34                          */
/*==============================================================*/


alter table MEILENSTEIN 
   drop foreign key FK_MEILENST_BILD_MEIL_BILD;

alter table MEILENSTEIN 
   drop foreign key FK_MEILENST_PROJEKT_M_PROJEKT;

alter table PROJEKT 
   drop foreign key FK_PROJEKT_NGA_PROJE_NGO;

alter table PROJEKT 
   drop foreign key FK_PROJEKT_PROJEKT_B_BILD;

alter table ZAHLUNG 
   drop foreign key FK_ZAHLUNG_ZAHLUNG_P_PROJEKT;

alter table ZAHLUNG 
   drop foreign key FK_ZAHLUNG_ZAHLUNG_U_USER;

alter table SOLUTION 
   drop foreign key FK_SOLUTION_SOLUTION_BILDSOLUTION_BILD;

alter table SUMMARY 
   drop foreign key FK_SUMMARY_SUMMARY_BILDSUMMARY_BILD;

alter table PROBLEM 
   drop foreign key FK_PROBLEM_PROBLEM_BILDPROBLEM_BILD

drop table if exists BILD;


alter table MEILENSTEIN 
   drop foreign key FK_MEILENST_PROJEKT_M_PROJEKT;

alter table MEILENSTEIN 
   drop foreign key FK_MEILENST_BILD_MEIL_BILD;

drop table if exists MEILENSTEIN;

drop table if exists NGO;


alter table PROJEKT 
   drop foreign key FK_PROJEKT_PROJEKT_B_BILD;

alter table PROJEKT 
   drop foreign key FK_PROJEKT_NGA_PROJE_NGO;

alter table PROJEKT 
   drop foreign key FK_PROJEKT_PROJEKT_PROB_PROBLEM;

alter table PROJEKT 
   drop foreign key FK_PROJEKT_PROJEKT_SM_SUMMARY;

alter table PROJEKT 
   drop foreign key FK_PROJEKT_PROJEKT_S_SOLUTION;


drop table if exists PROJEKT;

drop table id exists SUMMARY;

drop table id exists PROBLEM;

drop table id exists SOLUTION;


drop table if exists USER;

alter table ZAHLUNG 
   drop foreign key FK_ZAHLUNG_ZAHLUNG_P_PROJEKT;

alter table ZAHLUNG 
   drop foreign key FK_ZAHLUNG_ZAHLUNG_U_USER;

drop table if exists ZAHLUNG;

/*==============================================================*/
/* Table: BILD                                                  */
/*==============================================================*/
create table BILD
(
   BILD_ID              int not null  comment '',
   BILD_BILD            binary(0) not null  comment '',
   BILD_BESCHREIBUNG    varchar(256)  comment '',
   BILD_FORMAT          varchar(256)  comment '',
   primary key (BILD_ID)
);

/*==============================================================*/
/* Table: MEILENSTEIN                                           */
/*==============================================================*/
create table MEILENSTEIN
(
   MEILENSTEIN_ID       int not null  comment '',
   BILD_ID              int  comment '',
   PROJEKT_ID           int not null  comment '',
   MEILENSTEIN_NAME     varchar(256)  comment '',
   MEILENSTEIN_BETRAG   float not null  comment '',
   MEILENSTEIN_BESCHREIBUNG text  comment '',
   primary key (MEILENSTEIN_ID)
);

/*==============================================================*/
/* Table: NGO                                                   */
/*==============================================================*/
create table NGO
(
   NGO_ID               int not null  comment '',
   NGO_NAME             varchar(256) not null  comment '',
   NGO_EMAIL            varchar(256) not null  comment '',
   primary key (NGO_ID)
);

/*==============================================================*/
/* Table: SOLUTION                                              */
/*==============================================================*/
create table SOLUTION
(
   SOLUTION_ID          int not null comment '',
   SOLUTION_BESCHREIBUNG   text not full comment'',
   IMAGE_ID             int not not comment ''
   primary key (SOLUTION_ID)
);

/*==============================================================*/
/* Table: SUMMARY                                               */
/*==============================================================*/
create table SUMMARY
(
   SUMMARY_ID          int not null comment '',
   SUMMARY_BESCHREIBUNG   text not full comment'',
   IMAGE_ID             int not not comment ''
   primary key (SUMMARY_ID)
);

/*==============================================================*/
/* Table: PROBLEM                                               */
/*==============================================================*/
create table PROBLEM
(
   PROBLEM_ID          int not null comment '',
   PROBLEM_BESCHREIBUNG   text not full comment'',
   IMAGE_ID             int not not comment ''
   primary key (PROBLEM_ID)
);

/*==============================================================*/
/* Table: PROJEKT                                               */
/*==============================================================*/
create table PROJEKT
(
   PROJEKT_ID           int not null  comment '',
   NGO_ID               int not null  comment '',
   BILD_ID              int  comment '',
   SOLUTION_ID          int  comment '',
   SUMMARY_ID           int  comment '',
   PROBLEM_ID           int  comment '',
   PROJEKT_NAME         varchar(256)  comment '',
   PROJEKT_STATUS       bool not null  comment '',
   PROJEKT_ISTBETRAG    float  comment '',
   PROJEKT_SOLLBETRAG   float  comment '',
   PROJEKT_ZAHLUNGSINFORMATIONEN varchar(256)  comment '',
   PROJEKT_PAGE         varchar(256)  comment '',
   primary key (PROJEKT_ID)
);

/*==============================================================*/
/* Table: USER                                                  */
/*==============================================================*/
create table USER
(
   USER_ID              int not null  comment '',
   USER_VORNAME         varchar(256)  comment '',
   USER_NACHNAME        varchar(256)  comment '',
   USER_EMAIL           varchar(256) not null  comment '',
   USER_PASSWORDTOKEN   varchar(256) not null  comment '',
   USER_PUBLICKEY       varchar(256)  comment '',
   USER_PRIVATKEY       varchar(256)  comment '',
   USER_REGISTRIERTAM   date  comment '',
   primary key (USER_ID)
);

/*==============================================================*/
/* Table: ZAHLUNG                                               */
/*==============================================================*/
create table ZAHLUNG
(
   ZAHLUNG_ID           int not null  comment '',
   USER_ID              int not null  comment '',
   PROJEKT_ID           int not null  comment '',
   ZAHLUNG_BETRAG       float not null  comment '',
   ZAHLUNG_STATUS       varchar(256) not null  comment '',
   ZAHLUNG_DATUM        date  comment '',
   ZAHLUNG_UHRZEIT      time  comment '',
   primary key (ZAHLUNG_ID)
);



alter table MEILENSTEIN add constraint FK_MEILENST_BILD_MEIL_BILD foreign key (BILD_ID)
      references BILD (BILD_ID) on delete restrict on update restrict;

alter table MEILENSTEIN add constraint FK_MEILENST_PROJEKT_M_PROJEKT foreign key (PROJEKT_ID)
      references PROJEKT (PROJEKT_ID) on delete restrict on update restrict;

alter table PROJEKT add constraint FK_PROJEKT_NGA_PROJE_NGO foreign key (NGO_ID)
      references NGO (NGO_ID) on delete restrict on update restrict;

alter table PROJEKT add constraint FK_PROJEKT_PROJEKT_B_BILD foreign key (BILD_ID)
      references BILD (BILD_ID) on delete restrict on update restrict;

alter table PROJEKT add constraint FK_PROJEKT_PROJEKT_PROB_PROBLEM foreign key (PROBLEM_ID)
      references PROBLEM (PROBLEM_ID) on delete restrict on update restrict;

alter table PROJEKT add constraint FK_PROJEKT_PROJEKT_S_SOLUTION foreign key (SOLUTION_ID)
      references SOLUTION (SOLUTION_ID) on delete restrict on update restrict;

alter table PROJEKT add constraint FK_PROJEKT_PROJEKT_SM_SUMMARY foreign key (SUMMARY_ID)
      references SUMMARY (SUMMARY_ID) on delete restrict on update restrict;

alter table SOLUTION add constraint FK_SOLUTION_SOLUTION_BILDSOLUTION_BILD foreign key (BILD_ID)
      references BILD (BILD_ID) on delete restrict on update restrict;

alter table SUMMARY add constraint FK_SUMMARY_SUMMARY_BILDSUMMARY_BILD foreign key (BILD_ID)
      references BILD (BILD_ID) on delete restrict on update restrict;

alter table PROBLEM add constraint FK_PROBLEM_PROBLEM_BILDPROBLEM_BILD foreign key (BILD_ID)
      references BILD (BILD_ID) on delete restrict on update restrict;

alter table ZAHLUNG add constraint FK_ZAHLUNG_ZAHLUNG_P_PROJEKT foreign key (PROJEKT_ID)
      references PROJEKT (PROJEKT_ID) on delete restrict on update restrict;

alter table ZAHLUNG add constraint FK_ZAHLUNG_ZAHLUNG_U_USER foreign key (USER_ID)
      references USER (USER_ID) on delete restrict on update restrict;








