import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://expert-disco-x6j4vpxwv7jhqrg-8000.app.github.dev/api/teams/')
      .then(res => res.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div className="card mt-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Teams</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Name</th>
                <th>Members</th>
              </tr>
            </thead>
            <tbody>
              {teams.map(team => (
                <tr key={team._id}>
                  <td>{team.name}</td>
                  <td>{Array.isArray(team.members) ? team.members.join(', ') : ''}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Teams;
