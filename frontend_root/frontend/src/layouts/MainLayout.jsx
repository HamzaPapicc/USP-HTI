import { Outlet } from "react-router-dom";
import { useState } from "react";
import SideMenu from "../components/SideMenu";

function MainLayout()
{
    const [filters, setFilters] = useState({
        position_type: [],
        salary_min: "",
        salary_max: "",
    });

    return(
        <>
            <div>
                <SideMenu
                    filters={filters}
                    setFilters={setFilters}
                />
                <main>
                    <Outlet
                        context={{ filters, setFilters }}
                    />
                </main>
            </div>
        </>
    );
}

export default MainLayout;