import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const people = defineCollection({
  loader: glob({base:'./src/content/people',pattern:'**/*.md'}),
  schema: z.object({name:z.string(),role:z.string(),group:z.enum(['pi','postdoc','phd','research','alumni']),email:z.string().optional(),affiliation:z.string().optional(),status:z.enum(['current','former']),order:z.number().default(99),photo:z.string().optional(),scholar:z.string().optional(),orcid:z.string().optional(),github:z.string().optional(),website:z.string().optional(),interests:z.array(z.string()).default([])}),
});
const publications = defineCollection({
  loader: glob({base:'./src/content/publications',pattern:'**/*.md'}),
  schema: z.object({title:z.string(),authors:z.string(),year:z.number(),venue:z.string(),type:z.enum(['Journal','Conference','Preprint','Other']).default('Journal'),doi:z.string().optional(),url:z.string().optional(),bibtex:z.string().optional(),featured:z.boolean().default(false),draft:z.boolean().default(false)}),
});
const projects = defineCollection({
  loader: glob({base:'./src/content/projects',pattern:'**/*.md'}),
  schema:z.object({title:z.string(),eyebrow:z.string().default('Research theme'),summary:z.string(),area:z.string(),status:z.enum(['theme','active','completed']).default('theme'),featured:z.boolean().default(false),order:z.number().default(99)}),
});
const news = defineCollection({
  loader: glob({base:'./src/content/news',pattern:'**/*.md'}),
  schema:z.object({title:z.string(),date:z.coerce.date(),summary:z.string(),draft:z.boolean().default(false)}),
});
const collaborators = defineCollection({
  loader: glob({base:'./src/content/collaborators',pattern:'**/*.md'}),
  schema: z.object({
    name:z.string(), title:z.string().optional(), institution:z.string(),
    country:z.string().optional(), research:z.array(z.string()).default([]),
    website:z.string().optional(), scholar:z.string().optional(), orcid:z.string().optional(),
    photo:z.string().optional(), jointProjects:z.array(z.string()).default([]),
    featured:z.boolean().default(false), order:z.number().default(99)
  }),
});
export const collections = {people,publications,projects,news,collaborators};
