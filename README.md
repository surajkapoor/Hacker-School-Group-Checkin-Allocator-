Hacker-School-Group-Checkin-Allocator-
======================================

Deterministic approach that allocates students to a new group based on who they've checkin with before. The approach was to generate sets of groups at random. The default was to generate 10 sets but the user can overide that at the command line. 

Each set is given a score - if a student has checked in with another once, 10 points. Twice before is 100 points, and so on. Once the sets have been generated, the set of groups with the lowest score is chosen. 
