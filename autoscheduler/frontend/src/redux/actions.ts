import { Course } from '../types';
import {
  AddCourseAction, ADD_COURSE, RemoveCourseAction, REMOVE_COURSE,
} from './actionTypes';

// This file contains action creators: functions that can be called by React components
// via props and return Action objects that Redux can understand

export const addCourse = (course: Course): AddCourseAction => ({
  type: ADD_COURSE,
  course,
});

export const removeCourse = (course: Course): RemoveCourseAction => ({
  type: REMOVE_COURSE,
  course,
});
