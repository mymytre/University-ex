import express, {NextFunction, Request, Response} from "express";
import {User} from "../../model/user";


const router = express.Router();

router.post(
    "/api/users/signup",
    async (req: Request, res: Response, next: NextFunction) => {
        const {username, password} = req.body;
        const existingUser = await User.findOne({username});

        if (existingUser) {
            return next(new Error('Username in use'));
        }

        // Create User
        const user = User.build({
            username,
            password,
        })
        // Save in MongoDB
        await user.save();
        res.status(201).send({user})
    }
);

export {router as signupRouter};
