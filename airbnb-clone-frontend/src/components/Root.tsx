import {Link, Outlet} from "react-router-dom";
import {Box, Button, HStack} from "@chakra-ui/react";
import {FaAirbnb} from "react-icons/fa";

export default function Root() {
    return (
        <Box>
            <HStack
                justifyContent={"space-between"}
                py={5}
                px={10}
                borderBottomWidth={1}>
                <Box color="red.500">
                    <Link to={"/"}>
                        <FaAirbnb size={"48"}/>
                    </Link>
                </Box>
                <HStack>
                    <Button>Log in</Button>
                    <Button colorScheme={"red"}>Sign Up</Button>
                </HStack>
            </HStack>
            <Outlet/>
        </Box>
    );
}