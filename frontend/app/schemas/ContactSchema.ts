import { z } from "zod";

export const addContactSchema = z.object({
  name: z.string().min(1, "Name is required"),
  number: z
    .string()
    .min(10, "Please enter a valid phone number")
    .regex(/^[0-9]+$/, "Phone number must contain only digits 0-9"),
});

export type ContactFormData = z.infer<typeof addContactSchema>;
